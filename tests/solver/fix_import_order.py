from cutyjs.common.expand import expand
from cutyjs.models.content import Content
from cutyjs.solver.fix_import_order import fix_import_order

from langex.core.testing import discover_test, expects

original = """
import fs from "fs"
import React from "react"
import utils from "../utils"
import lodash from "lodash"
import App from "./App"
import "./styles.css"
import { Button } from "@/components/Button"
"""
expected = """import fs from "fs"

import lodash from "lodash"
import React from "react"

import { Button } from "@/components/Button"

import utils from "../utils"

import App from "./App"

import "./styles.css"


"""
received = fix_import_order(Content(original))
received = expand(received)

@discover_test
def test_fix_import_order():
  (lambda: received.content) @expects (expected)

