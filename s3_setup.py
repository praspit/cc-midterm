import sys
conf_file = "/var/www/html/wordpress/wp-config.php"

def main():
    access_key = sys.argv[1]
    secret_key = sys.argv[2]
    bucket_name = sys.argv[3]
    region = sys.argv[4]
    contents = ""
    with open(conf_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "define( 'WP_DEBUG', false );" in line:
                contents += (f"define( 'AS3CF_SETTINGS', serialize( array (\n")
                contents += (f"  'provider' => 'aws',\n")
                contents += (f"  'access-key-id' => '{access_key}',\n")
                contents += (f"  'secret-access-key' => '{secret_key}',\n")
                contents += (f"  'bucket' => '{bucket_name}',\n")
                contents += (f"  'region' => '{region}',\n")
                contents += (f"  'copy-to-s3' => true,\n")
                contents += (f"  'serve-from-s3' => true,\n")
                contents += (f") ) );\n")
            else:
                contents += line

    with open(conf_file, "w") as f:
        f.write(contents)

if __name__ == "__main__":
    main()
