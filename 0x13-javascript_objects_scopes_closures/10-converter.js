#!/usr/bin/node
'use strict';

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
