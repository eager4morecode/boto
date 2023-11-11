import boto3

def list_s3_buckets():
    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Call S3 to list the buckets
        response = s3.list_buckets()

        print("S3 Buckets:")
        for bucket in response['Buckets']:
            print(f" - {bucket['Name']}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_s3_buckets()
