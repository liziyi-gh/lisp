test:
	@echo -e "test basic"
	@cd test_lisp && python test_basic.py
	@echo -e "\ntest lambda"
	@cd test_lisp && python test_lambda.py
