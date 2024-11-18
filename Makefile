.PHONY: all
all: build ## Build the site (default target)

.PHONY: build
build: ## Build the Hugo site
	@hugo

.PHONY: serve run dev
serve run dev: ## Run the local Hugo development server
	@hugo serve

.PHONY: log
log: ## Create log post
	@python scripts/log.py

.PHONY: til
til: ## Create a new TIL (Today I Learned) post
	@python scripts/til.py $(p)

.PHONY: sync
sync: ## Sync content with Obsidian vault
	@unison content "/Users/danielcorin/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian/30 Resources/blog" -batch -auto -prefer newer

.PHONY: post
post: ## Create a new blog post
	@hugo new "posts/$(shell date +%Y)/$(p).md"

.PHONY: db
db: ## Build the site sqlite database
	@python scripts/build_database.py

.PHONY: tags
tags: ## List all tags used in the blog
	python -m scripts.list_tags

.PHONY: images
images: ## Optimize images in the specified directory (usage: make images d=path/to/dir)
	find $(d) -type f -name "*.png" -exec pngquant --quality=65-80 --ext=.png --force {} \;
	find $(d) -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) -exec jpegoptim --max=80 --strip-all {} \;
	find $(d) -type f -name "*.gif" -exec gifsicle -O3 --colors 256 -o {} {} \;

.PHONY: nbs
nbs: ## Convert Jupyter notebooks to posts
	@find content -name "*.ipynb" -print0 | xargs -0 -P 4 -I {} python -m scripts.convert_notebook {}

.PHONY: help
help: ## Display this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'
