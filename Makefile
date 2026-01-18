CLASSES := EENG4312 PHIL2306

SITE_DIR := site

.PHONY: all clean $(CLASSES) $(SITE_DIR)

all: $(CLASSES)

$(CLASSES):
	$(MAKE) -C $@ all

clean:
	for class in $(CLASSES); do \
		$(MAKE) -C $$class clean; \
	done
	@rm -rf $(SITE_DIR)

# Build everything and assemble the site (PDFs + index.html)
site: all
	@mkdir -p $(SITE_DIR)
	@echo "Collecting PDFs into $(SITE_DIR)/"
	@for class in $(CLASSES); do \
		pdf="$$class/build/main.pdf"; \
		if [ -f "$$pdf" ]; then \
			cp "$$pdf" "$(SITE_DIR)/main.pdf"; \
			echo "Found: $$pdf"; \
		else \
			echo "Warning: $$pdf not found" >&2; \
		fi; \
	done
	@echo "Generating HTML index"
	python3 tools/gen_index.py $(SITE_DIR) $(CLASSES)
