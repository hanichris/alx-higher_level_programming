#!/usr/bin/node
'use strict';

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    super.print(c);
  }
}

module.exports = Square;
