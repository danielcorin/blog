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
