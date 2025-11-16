.PHONY: EENG4312 all clean

CLASSES := EENG4312

$(CLASSES):
	$(MAKE) -C $@ all

clean:
	for class in $(CLASSES); do \
		$(MAKE) -C $$class clean; \
	done
