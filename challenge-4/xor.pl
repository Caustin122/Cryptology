#!/usr/bin/perl -0777 -p

# set variable for key filename
my $KEYNAME = "puzzle_encrypted";

# open key file for read-only access, and
# exit on file read error
open(my $KEY, '<', $KEYNAME)
    or die "Could not open file '$KEYNAME' $!";
# set file to binary mode for backward compatibility
binmode($KEY);
print <$KEY>; # Debug

# this is the tricky part, we modify the default
# argument/space, which has STDIN held within, 
# by reading the key file as a <FILEHANDLE>,
# which returns the entire key file, or a list of all lines
# in the file, which we XOR.
$_ ^= <$KEY>;

# close file for cleanup, and throw exception
# on error
close($KEY) || warn "close failed: $!";
