---
title: "Language model schema extraction and object generation"
date: 2023-03-04T08:01:17-05:00
tags:
  - language_models
  - gpt3
  - chatgpt
  - json_schema
  - python
  - openai
draft: false
---

I spent the week hacking on a languange model use case for structured data generation.
It turns out the structured data we hoped to generate didn't have a well-defined schema.
For the languange model to have any chance of suceess, it felt important to construct a schema definition as guide for the structure of the output.
However, manually extracting a schema definition for a complex object can tedious.
We were able to use the language model for this task.

## Using a language model to extract a JSON Schema by example

By feeding in several (PII sanitized) example objects and instructure the language model to define a [JSON schema](https://json-schema.org/) for those object, we were able to get most of the way to extracting a universal schema definition for these objects using `text-davinci-003`.

Here's a simple example of how you can do this:

{{< gist danielcorin 5329d185b19d7a768fb69ecc3326ff73 >}}

The output schema I got for my run of the language model is as follows:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "price": {
      "type": "number"
    },
    "brand": {
      "type": "string"
    },
    "category": {
      "type": "string"
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "image": {
      "type": "string"
    },
    "variants": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/variant"
      }
    }
  },
  "required": [
    "id",
    "name",
    "description",
    "price",
    "brand",
    "category",
    "tags",
    "image",
    "variants"
  ],
  "definitions": {
    "variant": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "price": {
          "type": "number"
        },
        "image": {
          "type": "string"
        },
        "options": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/option"
          }
        }
      },
      "required": [
        "id",
        "name",
        "price",
        "image",
        "options"
      ]
    },
    "option": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "values": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "values"
      ]
    }
  }
}
```

You may argue this schema isn't perfect structurally or that there are better ways to define schemas for JSON objects, but I think that is besides the point for the moment.
This schema an extremely helpful starting point and I separately validated that all the objects I passed into the prompt adhere to this schema.
In my experience, the more variety in the examples provide in the prompt, the better the result from the language model.
The main limiting factor for improvements with this method is the [maximum number of request tokens](https://platform.openai.com/docs/models/gpt-3-5) allowable by the model.

## Structured data generation

Returning to the original claim and promise -- let's use a language model for structured data generation.
Say I wanted to create some items for this e-commerce website using the schema the languange model extracted.
I could write some JSON by hand.
I could build a fancy UI form and using autocompletion to help speed up filling in all the fields.
I could build a file uploader and design an file upload schema then transform all my product descriptions to match that, then transform the uploaded file into the JSON schema.
All of the above are time consuming and often error prone, yet I've seen production systems that have made use of all of these approaches.
I know in the end I need objects with my schema described above, so let's see if we can go straight from product description to valid JSON objects.

Take [this product](https://www.apple.com/newsroom/2005/09/07Apple-Introduces-iPod-nano/) announcement from Apple for the iPod Nano.
Let's write a prompt for the language model to extract the product data:

{{< gist danielcorin 41d55cc9a0429dcead43601acbbf621c >}}

The output when run:

```json
{
  "id": 1,
  "name": "iPod nano",
  "description": "The iPod nano is a revolutionary full-featured iPod that holds 1,000 songs yet is thinner than a standard #2 pencil and less than half the size of competitive players.",
  "price": 249,
  "brand": "Apple",
  "category": "Music Player",
  "tags": [
    "ultra-portable",
    "lightweight",
    "gorgeous color screen",
    "Click Wheel"
  ],
  "image": "https://www.apple.com/v/ipod-nano/a/images/overview/ipod_nano_large.jpg",
  "variants": [
    {
      "id": 1,
      "name": "4GB",
      "price": 249,
      "image": "https://www.apple.com/v/ipod-nano/a/images/overview/ipod_nano_large.jpg",
      "options": [
        {
          "name": "Color",
          "values": [
            "White",
            "Black"
          ]
        }
      ]
    },
    {
      "id": 2,
      "name": "2GB",
      "price": 199,
      "image": "https://www.apple.com/v/ipod-nano/a/images/overview/ipod_nano_large.jpg",
      "options": [
        {
          "name": "Color",
          "values": [
            "White",
            "Black"
          ]
        }
      ]
    }
  ]
}
```

Pretty cool.
Is this perfect?
No.
The `id`s aren't really what you'd want.
Maybe you'd also want it to extract data for the last sentence about the lanyard headphones and armbands (bonus points if you even noticed that).
I don't think I'd necessarily want Apple's copy "gorgeous color screen" on my third party reseller website.
What is impressive and exciting is how trivial this capability is to build with a language model.

A fun note: the data schema and example JSON objects I used were [generated by ChatGPT](https://sharegpt.com/c/ETkymML).

## What's next?

- In the middle of last week, OpenAI released a ChatGPT API (`gpt-3.5-turbo`). I spent some time trying to port a similar type of data generation use case to the new API, but in the end, wasn't able to get as good results. I'd like to write up what this experience was like and do some more investigation on the API's capabilities.
- I still haven't had the chance to try and deploy pre-trained models from [Hugging Face](https://huggingface.co/) or investigating different types of models, but that is still something I am hoping to find the time to do.
- Writing up some more summaries and commentary on content I've enjoyed reading.
