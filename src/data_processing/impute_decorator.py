def imputation_decorator(imputation_class):
    def decorator(func):
        def wrapper(df, column):
            imputation_instance = imputation_class()
            imputation_instance.apply(df, column)
            return func(df, column)
        return wrapper
    return decorator
