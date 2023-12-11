LOCAL_JSON_SCHEMA_STORE = {
    "https://json-schema.org/draft/2019-09/schema": {
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$id": "https://json-schema.org/draft/2019-09/schema",
        "$vocabulary": {
            "https://json-schema.org/draft/2019-09/vocab/core": True,
            "https://json-schema.org/draft/2019-09/vocab/applicator": True,
            "https://json-schema.org/draft/2019-09/vocab/validation": True,
            "https://json-schema.org/draft/2019-09/vocab/meta-data": True,
            "https://json-schema.org/draft/2019-09/vocab/format": False,
            "https://json-schema.org/draft/2019-09/vocab/content": True
        },
        "$recursiveAnchor": True,
        "title": "Core and Validation specifications meta-schema",
        "allOf": [
            {
                "$ref": "meta/core"
            },
            {
                "$ref": "meta/applicator"
            },
            {
                "$ref": "meta/validation"
            },
            {
                "$ref": "meta/meta-data"
            },
            {
                "$ref": "meta/format"
            },
            {
                "$ref": "meta/content"
            }
        ],
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "definitions": {
                "$comment": "While no longer an official keyword as it is replaced by $defs, this keyword is retained in the meta-schema to prevent incompatible extensions as it remains in common use.",
                "type": "object",
                "additionalProperties": {
                    "$recursiveRef": "#"
                },
                "default": {}
            },
            "dependencies": {
                "$comment": "\"dependencies\" is no longer a keyword, but schema authors should avoid redefining it to facilitate a smooth transition to \"dependentSchemas\" and \"dependentRequired\"",
                "type": "object",
                "additionalProperties": {
                    "anyOf": [
                        {
                            "$recursiveRef": "#"
                        },
                        {
                            "$ref": "meta/validation#/$defs/stringArray"
                        }
                    ]
                }
            }
        }
    },
    "https://json-schema.org/draft/2019-09/meta/content": {
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$id": "https://json-schema.org/draft/2019-09/meta/content",
        "$vocabulary": {
            "https://json-schema.org/draft/2019-09/vocab/content": True
        },
        "$recursiveAnchor": True,
        "title": "Content vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "contentMediaType": {
                "type": "string"
            },
            "contentEncoding": {
                "type": "string"
            },
            "contentSchema": {
                "$recursiveRef": "#"
            }
        }
    },
    "https://json-schema.org/draft/2019-09/meta/format": {
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$id": "https://json-schema.org/draft/2019-09/meta/format",
        "$vocabulary": {
            "https://json-schema.org/draft/2019-09/vocab/format": True
        },
        "$recursiveAnchor": True,
        "title": "Format vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "format": {
                "type": "string"
            }
        }
    },
    "https://json-schema.org/draft/2020-12/meta/unevaluated": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://json-schema.org/draft/2020-12/meta/unevaluated",
        "$vocabulary": {
            "https://json-schema.org/draft/2020-12/vocab/unevaluated": True
        },
        "$dynamicAnchor": "meta",
        "title": "Unevaluated applicator vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "unevaluatedItems": {
                "$dynamicRef": "#meta"
            },
            "unevaluatedProperties": {
                "$dynamicRef": "#meta"
            }
        }
    },
    "https://json-schema.org/draft/2019-09/meta/validation": {
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$id": "https://json-schema.org/draft/2019-09/meta/validation",
        "$vocabulary": {
            "https://json-schema.org/draft/2019-09/vocab/validation": True
        },
        "$recursiveAnchor": True,
        "title": "Validation vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "multipleOf": {
                "type": "number",
                "exclusiveMinimum": 0
            },
            "maximum": {
                "type": "number"
            },
            "exclusiveMaximum": {
                "type": "number"
            },
            "minimum": {
                "type": "number"
            },
            "exclusiveMinimum": {
                "type": "number"
            },
            "maxLength": {
                "$ref": "#/$defs/nonNegativeInteger"
            },
            "minLength": {
                "$ref": "#/$defs/nonNegativeIntegerDefault0"
            },
            "pattern": {
                "type": "string",
                "format": "regex"
            },
            "maxItems": {
                "$ref": "#/$defs/nonNegativeInteger"
            },
            "minItems": {
                "$ref": "#/$defs/nonNegativeIntegerDefault0"
            },
            "uniqueItems": {
                "type": "boolean",
                "default": False
            },
            "maxContains": {
                "$ref": "#/$defs/nonNegativeInteger"
            },
            "minContains": {
                "$ref": "#/$defs/nonNegativeInteger",
                "default": 1
            },
            "maxProperties": {
                "$ref": "#/$defs/nonNegativeInteger"
            },
            "minProperties": {
                "$ref": "#/$defs/nonNegativeIntegerDefault0"
            },
            "required": {
                "$ref": "#/$defs/stringArray"
            },
            "dependentRequired": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#/$defs/stringArray"
                }
            },
            "const": True,
            "enum": {
                "type": "array",
                "items": True
            },
            "type": {
                "anyOf": [
                    {
                        "$ref": "#/$defs/simpleTypes"
                    },
                    {
                        "type": "array",
                        "items": {
                            "$ref": "#/$defs/simpleTypes"
                        },
                        "minItems": 1,
                        "uniqueItems": True
                    }
                ]
            }
        },
        "$defs": {
            "nonNegativeInteger": {
                "type": "integer",
                "minimum": 0
            },
            "nonNegativeIntegerDefault0": {
                "$ref": "#/$defs/nonNegativeInteger",
                "default": 0
            },
            "simpleTypes": {
                "enum": [
                    "array",
                    "boolean",
                    "integer",
                    "null",
                    "number",
                    "object",
                    "string"
                ]
            },
            "stringArray": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "uniqueItems": True,
                "default": []
            }
        }
    },
    "http://json-schema.org/draft-06/schema": {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "$id": "http://json-schema.org/draft-06/schema#",
        "title": "Core schema meta-schema",
        "definitions": {
            "schemaArray": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "$ref": "#"
                }
            },
            "nonNegativeInteger": {
                "type": "integer",
                "minimum": 0
            },
            "nonNegativeIntegerDefault0": {
                "allOf": [
                    {
                        "$ref": "#/definitions/nonNegativeInteger"
                    },
                    {
                        "default": 0
                    }
                ]
            },
            "simpleTypes": {
                "enum": [
                    "array",
                    "boolean",
                    "integer",
                    "null",
                    "number",
                    "object",
                    "string"
                ]
            },
            "stringArray": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "uniqueItems": True,
                "default": []
            }
        },
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "$id": {
                "type": "string",
                "format": "uri-reference"
            },
            "$schema": {
                "type": "string",
                "format": "uri"
            },
            "$ref": {
                "type": "string",
                "format": "uri-reference"
            },
            "title": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "default": {},
            "examples": {
                "type": "array",
                "items": {}
            },
            "multipleOf": {
                "type": "number",
                "exclusiveMinimum": 0
            },
            "maximum": {
                "type": "number"
            },
            "exclusiveMaximum": {
                "type": "number"
            },
            "minimum": {
                "type": "number"
            },
            "exclusiveMinimum": {
                "type": "number"
            },
            "maxLength": {
                "$ref": "#/definitions/nonNegativeInteger"
            },
            "minLength": {
                "$ref": "#/definitions/nonNegativeIntegerDefault0"
            },
            "pattern": {
                "type": "string",
                "format": "regex"
            },
            "additionalItems": {
                "$ref": "#"
            },
            "items": {
                "anyOf": [
                    {
                        "$ref": "#"
                    },
                    {
                        "$ref": "#/definitions/schemaArray"
                    }
                ],
                "default": {}
            },
            "maxItems": {
                "$ref": "#/definitions/nonNegativeInteger"
            },
            "minItems": {
                "$ref": "#/definitions/nonNegativeIntegerDefault0"
            },
            "uniqueItems": {
                "type": "boolean",
                "default": False
            },
            "contains": {
                "$ref": "#"
            },
            "maxProperties": {
                "$ref": "#/definitions/nonNegativeInteger"
            },
            "minProperties": {
                "$ref": "#/definitions/nonNegativeIntegerDefault0"
            },
            "required": {
                "$ref": "#/definitions/stringArray"
            },
            "additionalProperties": {
                "$ref": "#"
            },
            "definitions": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "default": {}
            },
            "properties": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "default": {}
            },
            "patternProperties": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "propertyNames": {
                    "format": "regex"
                },
                "default": {}
            },
            "dependencies": {
                "type": "object",
                "additionalProperties": {
                    "anyOf": [
                        {
                            "$ref": "#"
                        },
                        {
                            "$ref": "#/definitions/stringArray"
                        }
                    ]
                }
            },
            "propertyNames": {
                "$ref": "#"
            },
            "const": {},
            "enum": {
                "type": "array"
            },
            "type": {
                "anyOf": [
                    {
                        "$ref": "#/definitions/simpleTypes"
                    },
                    {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/simpleTypes"
                        },
                        "minItems": 1,
                        "uniqueItems": True
                    }
                ]
            },
            "format": {
                "type": "string"
            },
            "allOf": {
                "$ref": "#/definitions/schemaArray"
            },
            "anyOf": {
                "$ref": "#/definitions/schemaArray"
            },
            "oneOf": {
                "$ref": "#/definitions/schemaArray"
            },
            "not": {
                "$ref": "#"
            }
        },
        "default": {}
    },
    "https://json-schema.org/draft/2020-12/meta/format-annotation": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://json-schema.org/draft/2020-12/meta/format-annotation",
        "$vocabulary": {
            "https://json-schema.org/draft/2020-12/vocab/format-annotation": True
        },
        "$dynamicAnchor": "meta",
        "title": "Format vocabulary meta-schema for annotation results",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "format": {
                "type": "string"
            }
        }
    },
    "https://json-schema.org/draft/2020-12/meta/validation": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://json-schema.org/draft/2020-12/meta/validation",
        "$vocabulary": {
            "https://json-schema.org/draft/2020-12/vocab/validation": True
        },
        "$dynamicAnchor": "meta",
        "title": "Validation vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "type": {
                "anyOf": [
                    {
                        "$ref": "#/$defs/simpleTypes"
                    },
                    {
                        "type": "array",
                        "items": {
                            "$ref": "#/$defs/simpleTypes"
                        },
                        "minItems": 1,
                        "uniqueItems": True
                    }
                ]
            },
            "const": True,
            "enum": {
                "type": "array",
                "items": True
            },
            "multipleOf": {
                "type": "number",
                "exclusiveMinimum": 0
            },
            "maximum": {
                "type": "number"
            },
            "exclusiveMaximum": {
                "type": "number"
            },
            "minimum": {
                "type": "number"
            },
            "exclusiveMinimum": {
                "type": "number"
            },
            "maxLength": {
                "$ref": "#/$defs/nonNegativeInteger"
            },
            "minLength": {
                "$ref": "#/$defs/nonNegativeIntegerDefault0"
            },
            "pattern": {
                "type": "string",
                "format": "regex"
            },
            "maxItems": {
                "$ref": "#/$defs/nonNegativeInteger"
            },
            "minItems": {
                "$ref": "#/$defs/nonNegativeIntegerDefault0"
            },
            "uniqueItems": {
                "type": "boolean",
                "default": False
            },
            "maxContains": {
                "$ref": "#/$defs/nonNegativeInteger"
            },
            "minContains": {
                "$ref": "#/$defs/nonNegativeInteger",
                "default": 1
            },
            "maxProperties": {
                "$ref": "#/$defs/nonNegativeInteger"
            },
            "minProperties": {
                "$ref": "#/$defs/nonNegativeIntegerDefault0"
            },
            "required": {
                "$ref": "#/$defs/stringArray"
            },
            "dependentRequired": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#/$defs/stringArray"
                }
            }
        },
        "$defs": {
            "nonNegativeInteger": {
                "type": "integer",
                "minimum": 0
            },
            "nonNegativeIntegerDefault0": {
                "$ref": "#/$defs/nonNegativeInteger",
                "default": 0
            },
            "simpleTypes": {
                "enum": [
                    "array",
                    "boolean",
                    "integer",
                    "null",
                    "number",
                    "object",
                    "string"
                ]
            },
            "stringArray": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "uniqueItems": True,
                "default": []
            }
        }
    },
    "https://json-schema.org/draft/2020-12/meta/content": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://json-schema.org/draft/2020-12/meta/content",
        "$vocabulary": {
            "https://json-schema.org/draft/2020-12/vocab/content": True
        },
        "$dynamicAnchor": "meta",
        "title": "Content vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "contentEncoding": {
                "type": "string"
            },
            "contentMediaType": {
                "type": "string"
            },
            "contentSchema": {
                "$dynamicRef": "#meta"
            }
        }
    },
    "http://json-schema.org/draft-07/schema": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "http://json-schema.org/draft-07/schema#",
        "title": "Core schema meta-schema",
        "definitions": {
            "schemaArray": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "$ref": "#"
                }
            },
            "nonNegativeInteger": {
                "type": "integer",
                "minimum": 0
            },
            "nonNegativeIntegerDefault0": {
                "allOf": [
                    {
                        "$ref": "#/definitions/nonNegativeInteger"
                    },
                    {
                        "default": 0
                    }
                ]
            },
            "simpleTypes": {
                "enum": [
                    "array",
                    "boolean",
                    "integer",
                    "null",
                    "number",
                    "object",
                    "string"
                ]
            },
            "stringArray": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "uniqueItems": True,
                "default": []
            }
        },
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "$id": {
                "type": "string",
                "format": "uri-reference"
            },
            "$schema": {
                "type": "string",
                "format": "uri"
            },
            "$ref": {
                "type": "string",
                "format": "uri-reference"
            },
            "$comment": {
                "type": "string"
            },
            "title": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "default": True,
            "readOnly": {
                "type": "boolean",
                "default": False
            },
            "examples": {
                "type": "array",
                "items": True
            },
            "multipleOf": {
                "type": "number",
                "exclusiveMinimum": 0
            },
            "maximum": {
                "type": "number"
            },
            "exclusiveMaximum": {
                "type": "number"
            },
            "minimum": {
                "type": "number"
            },
            "exclusiveMinimum": {
                "type": "number"
            },
            "maxLength": {
                "$ref": "#/definitions/nonNegativeInteger"
            },
            "minLength": {
                "$ref": "#/definitions/nonNegativeIntegerDefault0"
            },
            "pattern": {
                "type": "string",
                "format": "regex"
            },
            "additionalItems": {
                "$ref": "#"
            },
            "items": {
                "anyOf": [
                    {
                        "$ref": "#"
                    },
                    {
                        "$ref": "#/definitions/schemaArray"
                    }
                ],
                "default": True
            },
            "maxItems": {
                "$ref": "#/definitions/nonNegativeInteger"
            },
            "minItems": {
                "$ref": "#/definitions/nonNegativeIntegerDefault0"
            },
            "uniqueItems": {
                "type": "boolean",
                "default": False
            },
            "contains": {
                "$ref": "#"
            },
            "maxProperties": {
                "$ref": "#/definitions/nonNegativeInteger"
            },
            "minProperties": {
                "$ref": "#/definitions/nonNegativeIntegerDefault0"
            },
            "required": {
                "$ref": "#/definitions/stringArray"
            },
            "additionalProperties": {
                "$ref": "#"
            },
            "definitions": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "default": {}
            },
            "properties": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "default": {}
            },
            "patternProperties": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "propertyNames": {
                    "format": "regex"
                },
                "default": {}
            },
            "dependencies": {
                "type": "object",
                "additionalProperties": {
                    "anyOf": [
                        {
                            "$ref": "#"
                        },
                        {
                            "$ref": "#/definitions/stringArray"
                        }
                    ]
                }
            },
            "propertyNames": {
                "$ref": "#"
            },
            "const": True,
            "enum": {
                "type": "array",
                "items": True
            },
            "type": {
                "anyOf": [
                    {
                        "$ref": "#/definitions/simpleTypes"
                    },
                    {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/simpleTypes"
                        },
                        "minItems": 1,
                        "uniqueItems": True
                    }
                ]
            },
            "format": {
                "type": "string"
            },
            "contentMediaType": {
                "type": "string"
            },
            "contentEncoding": {
                "type": "string"
            },
            "if": {
                "$ref": "#"
            },
            "then": {
                "$ref": "#"
            },
            "else": {
                "$ref": "#"
            },
            "allOf": {
                "$ref": "#/definitions/schemaArray"
            },
            "anyOf": {
                "$ref": "#/definitions/schemaArray"
            },
            "oneOf": {
                "$ref": "#/definitions/schemaArray"
            },
            "not": {
                "$ref": "#"
            }
        },
        "default": True
    },
    "http://json-schema.org/draft-04/schema": {
        "id": "http://json-schema.org/draft-04/schema#",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Core schema meta-schema",
        "definitions": {
            "schemaArray": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "$ref": "#"
                }
            },
            "positiveInteger": {
                "type": "integer",
                "minimum": 0
            },
            "positiveIntegerDefault0": {
                "allOf": [
                    {
                        "$ref": "#/definitions/positiveInteger"
                    },
                    {
                        "default": 0
                    }
                ]
            },
            "simpleTypes": {
                "enum": [
                    "array",
                    "boolean",
                    "integer",
                    "null",
                    "number",
                    "object",
                    "string"
                ]
            },
            "stringArray": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "minItems": 1,
                "uniqueItems": True
            }
        },
        "type": "object",
        "properties": {
            "id": {
                "type": "string"
            },
            "$schema": {
                "type": "string"
            },
            "title": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "default": {},
            "multipleOf": {
                "type": "number",
                "minimum": 0,
                "exclusiveMinimum": True
            },
            "maximum": {
                "type": "number"
            },
            "exclusiveMaximum": {
                "type": "boolean",
                "default": False
            },
            "minimum": {
                "type": "number"
            },
            "exclusiveMinimum": {
                "type": "boolean",
                "default": False
            },
            "maxLength": {
                "$ref": "#/definitions/positiveInteger"
            },
            "minLength": {
                "$ref": "#/definitions/positiveIntegerDefault0"
            },
            "pattern": {
                "type": "string",
                "format": "regex"
            },
            "additionalItems": {
                "anyOf": [
                    {
                        "type": "boolean"
                    },
                    {
                        "$ref": "#"
                    }
                ],
                "default": {}
            },
            "items": {
                "anyOf": [
                    {
                        "$ref": "#"
                    },
                    {
                        "$ref": "#/definitions/schemaArray"
                    }
                ],
                "default": {}
            },
            "maxItems": {
                "$ref": "#/definitions/positiveInteger"
            },
            "minItems": {
                "$ref": "#/definitions/positiveIntegerDefault0"
            },
            "uniqueItems": {
                "type": "boolean",
                "default": False
            },
            "maxProperties": {
                "$ref": "#/definitions/positiveInteger"
            },
            "minProperties": {
                "$ref": "#/definitions/positiveIntegerDefault0"
            },
            "required": {
                "$ref": "#/definitions/stringArray"
            },
            "additionalProperties": {
                "anyOf": [
                    {
                        "type": "boolean"
                    },
                    {
                        "$ref": "#"
                    }
                ],
                "default": {}
            },
            "definitions": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "default": {}
            },
            "properties": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "default": {}
            },
            "patternProperties": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "default": {}
            },
            "dependencies": {
                "type": "object",
                "additionalProperties": {
                    "anyOf": [
                        {
                            "$ref": "#"
                        },
                        {
                            "$ref": "#/definitions/stringArray"
                        }
                    ]
                }
            },
            "enum": {
                "type": "array",
                "minItems": 1,
                "uniqueItems": True
            },
            "type": {
                "anyOf": [
                    {
                        "$ref": "#/definitions/simpleTypes"
                    },
                    {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/simpleTypes"
                        },
                        "minItems": 1,
                        "uniqueItems": True
                    }
                ]
            },
            "format": {
                "type": "string"
            },
            "allOf": {
                "$ref": "#/definitions/schemaArray"
            },
            "anyOf": {
                "$ref": "#/definitions/schemaArray"
            },
            "oneOf": {
                "$ref": "#/definitions/schemaArray"
            },
            "not": {
                "$ref": "#"
            }
        },
        "dependencies": {
            "exclusiveMaximum": [
                "maximum"
            ],
            "exclusiveMinimum": [
                "minimum"
            ]
        },
        "default": {}
    },
    "https://json-schema.org/draft/2020-12/meta/format-assertion": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://json-schema.org/draft/2020-12/meta/format-assertion",
        "$vocabulary": {
            "https://json-schema.org/draft/2020-12/vocab/format-assertion": True
        },
        "$dynamicAnchor": "meta",
        "title": "Format vocabulary meta-schema for assertion results",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "format": {
                "type": "string"
            }
        }
    },
    "https://json-schema.org/draft/2020-12/meta/applicator": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://json-schema.org/draft/2020-12/meta/applicator",
        "$vocabulary": {
            "https://json-schema.org/draft/2020-12/vocab/applicator": True
        },
        "$dynamicAnchor": "meta",
        "title": "Applicator vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "prefixItems": {
                "$ref": "#/$defs/schemaArray"
            },
            "items": {
                "$dynamicRef": "#meta"
            },
            "contains": {
                "$dynamicRef": "#meta"
            },
            "additionalProperties": {
                "$dynamicRef": "#meta"
            },
            "properties": {
                "type": "object",
                "additionalProperties": {
                    "$dynamicRef": "#meta"
                },
                "default": {}
            },
            "patternProperties": {
                "type": "object",
                "additionalProperties": {
                    "$dynamicRef": "#meta"
                },
                "propertyNames": {
                    "format": "regex"
                },
                "default": {}
            },
            "dependentSchemas": {
                "type": "object",
                "additionalProperties": {
                    "$dynamicRef": "#meta"
                },
                "default": {}
            },
            "propertyNames": {
                "$dynamicRef": "#meta"
            },
            "if": {
                "$dynamicRef": "#meta"
            },
            "then": {
                "$dynamicRef": "#meta"
            },
            "else": {
                "$dynamicRef": "#meta"
            },
            "allOf": {
                "$ref": "#/$defs/schemaArray"
            },
            "anyOf": {
                "$ref": "#/$defs/schemaArray"
            },
            "oneOf": {
                "$ref": "#/$defs/schemaArray"
            },
            "not": {
                "$dynamicRef": "#meta"
            }
        },
        "$defs": {
            "schemaArray": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "$dynamicRef": "#meta"
                }
            }
        }
    },
    "https://json-schema.org/draft/2019-09/meta/applicator": {
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$id": "https://json-schema.org/draft/2019-09/meta/applicator",
        "$vocabulary": {
            "https://json-schema.org/draft/2019-09/vocab/applicator": True
        },
        "$recursiveAnchor": True,
        "title": "Applicator vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "additionalItems": {
                "$recursiveRef": "#"
            },
            "unevaluatedItems": {
                "$recursiveRef": "#"
            },
            "items": {
                "anyOf": [
                    {
                        "$recursiveRef": "#"
                    },
                    {
                        "$ref": "#/$defs/schemaArray"
                    }
                ]
            },
            "contains": {
                "$recursiveRef": "#"
            },
            "additionalProperties": {
                "$recursiveRef": "#"
            },
            "unevaluatedProperties": {
                "$recursiveRef": "#"
            },
            "properties": {
                "type": "object",
                "additionalProperties": {
                    "$recursiveRef": "#"
                },
                "default": {}
            },
            "patternProperties": {
                "type": "object",
                "additionalProperties": {
                    "$recursiveRef": "#"
                },
                "propertyNames": {
                    "format": "regex"
                },
                "default": {}
            },
            "dependentSchemas": {
                "type": "object",
                "additionalProperties": {
                    "$recursiveRef": "#"
                }
            },
            "propertyNames": {
                "$recursiveRef": "#"
            },
            "if": {
                "$recursiveRef": "#"
            },
            "then": {
                "$recursiveRef": "#"
            },
            "else": {
                "$recursiveRef": "#"
            },
            "allOf": {
                "$ref": "#/$defs/schemaArray"
            },
            "anyOf": {
                "$ref": "#/$defs/schemaArray"
            },
            "oneOf": {
                "$ref": "#/$defs/schemaArray"
            },
            "not": {
                "$recursiveRef": "#"
            }
        },
        "$defs": {
            "schemaArray": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "$recursiveRef": "#"
                }
            }
        }
    },
    "https://json-schema.org/draft/2020-12/meta/meta-data": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://json-schema.org/draft/2020-12/meta/meta-data",
        "$vocabulary": {
            "https://json-schema.org/draft/2020-12/vocab/meta-data": True
        },
        "$dynamicAnchor": "meta",
        "title": "Meta-data vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "title": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "default": True,
            "deprecated": {
                "type": "boolean",
                "default": False
            },
            "readOnly": {
                "type": "boolean",
                "default": False
            },
            "writeOnly": {
                "type": "boolean",
                "default": False
            },
            "examples": {
                "type": "array",
                "items": True
            }
        }
    },
    "https://json-schema.org/draft/2019-09/meta/meta-data": {
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$id": "https://json-schema.org/draft/2019-09/meta/meta-data",
        "$vocabulary": {
            "https://json-schema.org/draft/2019-09/vocab/meta-data": True
        },
        "$recursiveAnchor": True,
        "title": "Meta-data vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "title": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "default": True,
            "deprecated": {
                "type": "boolean",
                "default": False
            },
            "readOnly": {
                "type": "boolean",
                "default": False
            },
            "writeOnly": {
                "type": "boolean",
                "default": False
            },
            "examples": {
                "type": "array",
                "items": True
            }
        }
    },
    "https://json-schema.org/draft/2020-12/meta/core": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://json-schema.org/draft/2020-12/meta/core",
        "$vocabulary": {
            "https://json-schema.org/draft/2020-12/vocab/core": True
        },
        "$dynamicAnchor": "meta",
        "title": "Core vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "$id": {
                "$ref": "#/$defs/uriReferenceString",
                "$comment": "Non-empty fragments not allowed.",
                "pattern": "^[^#]*#?$"
            },
            "$schema": {
                "$ref": "#/$defs/uriString"
            },
            "$ref": {
                "$ref": "#/$defs/uriReferenceString"
            },
            "$anchor": {
                "$ref": "#/$defs/anchorString"
            },
            "$dynamicRef": {
                "$ref": "#/$defs/uriReferenceString"
            },
            "$dynamicAnchor": {
                "$ref": "#/$defs/anchorString"
            },
            "$vocabulary": {
                "type": "object",
                "propertyNames": {
                    "$ref": "#/$defs/uriString"
                },
                "additionalProperties": {
                    "type": "boolean"
                }
            },
            "$comment": {
                "type": "string"
            },
            "$defs": {
                "type": "object",
                "additionalProperties": {
                    "$dynamicRef": "#meta"
                }
            }
        },
        "$defs": {
            "anchorString": {
                "type": "string",
                "pattern": "^[A-Za-z_][-A-Za-z0-9._]*$"
            },
            "uriString": {
                "type": "string",
                "format": "uri"
            },
            "uriReferenceString": {
                "type": "string",
                "format": "uri-reference"
            }
        }
    },
    "https://json-schema.org/draft/2020-12/schema": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://json-schema.org/draft/2020-12/schema",
        "$vocabulary": {
            "https://json-schema.org/draft/2020-12/vocab/core": True,
            "https://json-schema.org/draft/2020-12/vocab/applicator": True,
            "https://json-schema.org/draft/2020-12/vocab/unevaluated": True,
            "https://json-schema.org/draft/2020-12/vocab/validation": True,
            "https://json-schema.org/draft/2020-12/vocab/meta-data": True,
            "https://json-schema.org/draft/2020-12/vocab/format-annotation": True,
            "https://json-schema.org/draft/2020-12/vocab/content": True
        },
        "$dynamicAnchor": "meta",
        "title": "Core and Validation specifications meta-schema",
        "allOf": [
            {
                "$ref": "meta/core"
            },
            {
                "$ref": "meta/applicator"
            },
            {
                "$ref": "meta/unevaluated"
            },
            {
                "$ref": "meta/validation"
            },
            {
                "$ref": "meta/meta-data"
            },
            {
                "$ref": "meta/format-annotation"
            },
            {
                "$ref": "meta/content"
            }
        ],
        "type": [
            "object",
            "boolean"
        ],
        "$comment": "This meta-schema also defines keywords that have appeared in previous drafts in order to prevent incompatible extensions as they remain in common use.",
        "properties": {
            "definitions": {
                "$comment": "\"definitions\" has been replaced by \"$defs\".",
                "type": "object",
                "additionalProperties": {
                    "$dynamicRef": "#meta"
                },
                "deprecated": True,
                "default": {}
            },
            "dependencies": {
                "$comment": "\"dependencies\" has been split and replaced by \"dependentSchemas\" and \"dependentRequired\" in order to serve their differing semantics.",
                "type": "object",
                "additionalProperties": {
                    "anyOf": [
                        {
                            "$dynamicRef": "#meta"
                        },
                        {
                            "$ref": "meta/validation#/$defs/stringArray"
                        }
                    ]
                },
                "deprecated": True,
                "default": {}
            },
            "$recursiveAnchor": {
                "$comment": "\"$recursiveAnchor\" has been replaced by \"$dynamicAnchor\".",
                "$ref": "meta/core#/$defs/anchorString",
                "deprecated": True
            },
            "$recursiveRef": {
                "$comment": "\"$recursiveRef\" has been replaced by \"$dynamicRef\".",
                "$ref": "meta/core#/$defs/uriReferenceString",
                "deprecated": True
            }
        }
    },
    "http://json-schema.org/draft-03/schema": {
        "$schema": "http://json-schema.org/draft-03/schema#",
        "id": "http://json-schema.org/draft-03/schema#",
        "type": "object",
        "properties": {
            "type": {
                "type": [
                    "string",
                    "array"
                ],
                "items": {
                    "type": [
                        "string",
                        {
                            "$ref": "#"
                        }
                    ]
                },
                "uniqueItems": True,
                "default": "any"
            },
            "properties": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "default": {}
            },
            "patternProperties": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "#"
                },
                "default": {}
            },
            "additionalProperties": {
                "type": [
                    {
                        "$ref": "#"
                    },
                    "boolean"
                ],
                "default": {}
            },
            "items": {
                "type": [
                    {
                        "$ref": "#"
                    },
                    "array"
                ],
                "items": {
                    "$ref": "#"
                },
                "default": {}
            },
            "additionalItems": {
                "type": [
                    {
                        "$ref": "#"
                    },
                    "boolean"
                ],
                "default": {}
            },
            "required": {
                "type": "boolean",
                "default": False
            },
            "dependencies": {
                "type": "object",
                "additionalProperties": {
                    "type": [
                        "string",
                        "array",
                        {
                            "$ref": "#"
                        }
                    ],
                    "items": {
                        "type": "string"
                    }
                },
                "default": {}
            },
            "minimum": {
                "type": "number"
            },
            "maximum": {
                "type": "number"
            },
            "exclusiveMinimum": {
                "type": "boolean",
                "default": False
            },
            "exclusiveMaximum": {
                "type": "boolean",
                "default": False
            },
            "minItems": {
                "type": "integer",
                "minimum": 0,
                "default": 0
            },
            "maxItems": {
                "type": "integer",
                "minimum": 0
            },
            "uniqueItems": {
                "type": "boolean",
                "default": False
            },
            "pattern": {
                "type": "string",
                "format": "regex"
            },
            "minLength": {
                "type": "integer",
                "minimum": 0,
                "default": 0
            },
            "maxLength": {
                "type": "integer"
            },
            "enum": {
                "type": "array",
                "minItems": 1,
                "uniqueItems": True
            },
            "default": {
                "type": "any"
            },
            "title": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "format": {
                "type": "string"
            },
            "divisibleBy": {
                "type": "number",
                "minimum": 0,
                "exclusiveMinimum": True,
                "default": 1
            },
            "disallow": {
                "type": [
                    "string",
                    "array"
                ],
                "items": {
                    "type": [
                        "string",
                        {
                            "$ref": "#"
                        }
                    ]
                },
                "uniqueItems": True
            },
            "extends": {
                "type": [
                    {
                        "$ref": "#"
                    },
                    "array"
                ],
                "items": {
                    "$ref": "#"
                },
                "default": {}
            },
            "id": {
                "type": "string"
            },
            "$ref": {
                "type": "string"
            },
            "$schema": {
                "type": "string",
                "format": "uri"
            }
        },
        "dependencies": {
            "exclusiveMinimum": "minimum",
            "exclusiveMaximum": "maximum"
        },
        "default": {}
    },
    "https://json-schema.org/draft/2019-09/meta/core": {
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$id": "https://json-schema.org/draft/2019-09/meta/core",
        "$vocabulary": {
            "https://json-schema.org/draft/2019-09/vocab/core": True
        },
        "$recursiveAnchor": True,
        "title": "Core vocabulary meta-schema",
        "type": [
            "object",
            "boolean"
        ],
        "properties": {
            "$id": {
                "type": "string",
                "format": "uri-reference",
                "$comment": "Non-empty fragments not allowed.",
                "pattern": "^[^#]*#?$"
            },
            "$schema": {
                "type": "string",
                "format": "uri"
            },
            "$anchor": {
                "type": "string",
                "pattern": "^[A-Za-z][-A-Za-z0-9.:_]*$"
            },
            "$ref": {
                "type": "string",
                "format": "uri-reference"
            },
            "$recursiveRef": {
                "type": "string",
                "format": "uri-reference"
            },
            "$recursiveAnchor": {
                "type": "boolean",
                "default": False
            },
            "$vocabulary": {
                "type": "object",
                "propertyNames": {
                    "type": "string",
                    "format": "uri"
                },
                "additionalProperties": {
                    "type": "boolean"
                }
            },
            "$comment": {
                "type": "string"
            },
            "$defs": {
                "type": "object",
                "additionalProperties": {
                    "$recursiveRef": "#"
                },
                "default": {}
            }
        }
    },
    "https://json-schema.org/draft/2019-09/links": "https://json-schema.org/draft/2019-09/links"
}