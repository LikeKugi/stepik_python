def info_kwargs(**kwargs):
    [print(f'{key} = {value}') for key, value in sorted(kwargs.items(), key=lambda x: x[0])]


info_kwargs(first_name="John", last_name="Doe", age=33)
