CLASSES := EENG4312 PHIL2306
# Non-course reference books (project notes, design write-ups)
REFERENCE := EMIFilter
NOTES := $(CLASSES) $(REFERENCE)

SITE_DIR := site

.PHONY: all clean $(NOTES) $(SITE_DIR)

all: $(NOTES)

$(NOTES):
	$(MAKE) -C $@ all

clean:
	for class in $(NOTES); do \
		$(MAKE) -C $$class clean; \
	done
	@rm -rf $(SITE_DIR)

# Build everything and assemble the site (PDFs + index.html)
site: all
	@mkdir -p $(SITE_DIR)
	@echo "Collecting PDFs into $(SITE_DIR)/"
	@for class in $(NOTES); do \
		pdf="$$class/build/main.pdf"; \
		if [ -f "$$pdf" ]; then \
			cp "$$pdf" "$(SITE_DIR)/$$class.pdf"; \
			echo "Found: $$pdf"; \
		else \
			echo "Warning: $$pdf not found" >&2; \
		fi; \
	done
	@echo "Generating HTML index"
	python3 tools/gen_index.py $(SITE_DIR) $(NOTES)
