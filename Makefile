# Default target
.PHONY: all
all: build

# Build the site
.PHONY: build
build:
	@hugo

# Run the local development server
.PHONY: serve run dev
serve run dev:
	@hugo serve

.PHONY: log
log:
	@python scripts/log.py

.PHONY: til
til:
	@python scripts/til.py $(p)

.PHONY: sync
sync:
	@unison content "/Users/danielcorin/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian/30 Resources/blog" -batch -auto -prefer newer

.PHONY: post
post:
	@hugo new "posts/$(shell date +%Y)/$(p).md"

.PHONY: db
db:
	@python scripts/build_database.py

.PHONY: tags
tags:
	python -m scripts.list_tags

.PHONY: images
images:
	find _static/img -type f -name "*.png" -exec pngquant --quality=65-80 --ext=.png --force {} \;
	find _static/img -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) -exec jpegoptim --max=80 --strip-all {} \;
	find _static/img -type f -name "*.gif" -exec gifsicle -O3 --colors 256 -o {} {} \;
