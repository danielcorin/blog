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

