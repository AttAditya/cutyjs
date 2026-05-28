from cutyjs.common.expand import expand
from cutyjs.models.content import Content
from cutyjs.solver.fix_import_order import fix_import_order

from langex.core.testing import discover_test, expects

def test_basic():
  original = """
  import fs from "fs"
  import React from "react"
  import utils from "../utils"
  import lodash from "lodash"
  import App from "./App"
  import "./styles.css"
  import { Button } from "@/components/Button"
  """.replace("\n  ", "\n")
  expected = """import fs from "fs"

  import lodash from "lodash"
  import React from "react"

  import { Button } from "@/components/Button"

  import utils from "../utils"

  import App from "./App"

  import "./styles.css"


  """.replace("\n  ", "\n")
  received = fix_import_order(Content(original))
  received = expand(received).content

  return received == expected

def test_types():
  original = """
  import {
    Button,
    Input,
    Textarea,
  } from "@/components"
  import type {
    User,
    Post,
  } from "@/types"
  """.replace("\n  ", "\n")
  expected = """import {
    Button,
    Input,
    Textarea,
  } from "@/components"
  import type {
    User,
    Post,
  } from "@/types"


  """.replace("\n  ", "\n")
  received = fix_import_order(Content(original))
  received = expand(received).content

  return received == expected

@discover_test
def test_fix_import_order():
  test_basic @expects (True)
  test_types @expects (True)

