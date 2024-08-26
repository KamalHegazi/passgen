#!/bin/sh

# Make the passgen.py script executable
chmod 777 passgen.py

# Create the directory for passgen
mkdir -p /usr/share/passgen

# Copy the passgen.py script to the new directory
cp passgen.py /usr/share/passgen/passgen.py

# Create the shell script to execute passgen.py
echo '#!/bin/sh\nexec python3 /usr/share/passgen/passgen.py "$@"' > /usr/bin/passgen

# Make the new scripts executable
chmod +x /usr/bin/passgen
chmod +x /usr/share/passgen/passgen.py

echo "Done!"

