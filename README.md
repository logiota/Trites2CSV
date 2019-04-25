# Trytes2CSV
Translate trytes directly to alphanumeric characters and keep the trytes somewhat readable directly in a tangle explorer.

This will help run projects on small devices doing datalogging by reducing the pow for larger than 440 Bytes of data.

A csv file in a single transaction can now contain 670 double digit measurements or at least 2000 characters.

This is an example of data turnary:
XTEXT9SXAS9SXTEXT9SABCDEFJABC

Which should result in the following ASCII data:
TEXT AS TEXT 123456,123
