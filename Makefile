PY?=python
PELICAN?=poetry run pelican
PELICANOPTS=
GHP_IMPORT?=poetry run ghp-import
JUPYTER?=poetry run jupyter

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_HOST=localhost
SSH_PORT=22
SSH_USER=chris
SSH_TARGET_DIR=/var/www

GITHUB_PAGES_BRANCH=master

ifdef THEME
	PELICANOPTS += -t $(THEME)
endif

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

ifdef PORT
	PELICANOPTS += -p $(PORT)
endif

help:
	@echo '                                                                                '
	@echo ' Makefile for a pelican Web site                                                '
	@echo '                                                                                '
	@echo ' Usage:                                                                         '
	@echo ' make html                           (re)generate the web site                  '
	@echo ' make ipynb_clean                    clear output of all jupyter notebooks      '
	@echo ' make fresh                          clear output and execute jupyter notebooks '
	@echo ' make clean                          remove the generated files                 '
	@echo ' make regenerate                     regenerate files upon modification         '
	@echo ' make publish                        generate using production settings         '
	@echo ' make serve [PORT=8000]              serve site at http://localhost:8000        '
	@echo ' make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80            '
	@echo ' make devserver [PORT=8000]          serve and regenerate together              '
	@echo ' make ssh_upload                     upload the web site via SSH                '
	@echo ' make rsync_upload                   upload the web site via rsync+ssh          '
	@echo ' make github                         upload the web site via gh-pages           '
	@echo '                                                                                '
	@echo ' Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html        '
	@echo ' Set the RELATIVE variable to 1 to enable relative urls                         '
	@echo '                                                                                '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

ipynb_clean:
	find $(INPUTDIR) \( -name '*.ipynb' -and ! -name '*checkpoint*' \) \
		-exec $(JUPYTER) nbconvert \
		--ClearOutputPreprocessor.enabled=True \
		--inplace \
		{} \;

fresh: ipynb_clean
	find $(INPUTDIR) \( -name '*.ipynb' -and ! -name '*checkpoint*' \) \
		-exec $(JUPYTER) nbconvert \
		--execute \
		--inplace \
		{} \;

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve-global:
ifdef SERVER
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b $(SERVER)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b 0.0.0.0
endif


devserver:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

ssh_upload: publish
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --cvs-exclude --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

github: fresh publish
	$(GHP_IMPORT) -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)


.PHONY: html help clean regenerate serve serve-global devserver publish ssh_upload rsync_upload github
