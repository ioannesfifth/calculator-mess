from jsonschema import Draft202012Validator, validators

def is_function(_, instance):
    return callable(instance)

ExtendedValidator = validators.extend(
    Draft202012Validator, # default validator
    type_checker=Draft202012Validator.TYPE_CHECKER.redefine("function", is_function)
)