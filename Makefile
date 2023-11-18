# Default target
.PHONY: all
all: build

# Build the site
.PHONY: build
build:
	@hugo

# Run the local development server
.PHONY: serve run
serve run:
	@hugo serve

.PHONY: log
log:
	@python scripts/log.py

.PHONY: til
til:
	@python scripts/til.py $(p)

