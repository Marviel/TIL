def bucket_name_from_url(url):
    """
    Gets bucketName, region, and keyName from url, matching any of the different formats for S3 urls
    * http://bucket.s3.amazonaws.com
    * http://bucket.s3-aws-region.amazonaws.com
    * http://s3.amazonaws.com/bucket
    * http://s3-aws-region.amazonaws.com/bucket

    returns bucketName, region, keyName
    
    
    (adapted from https://stackoverflow.com/a/28052370/2665476)
    """
    match =  re.search('^https?://(.+).s3.amazonaws.com/', url)
    if match:
        return match.group(1), None, None

    match =  re.search('^https?://(.+).s3-([^.]+).amazonaws.com/(.+)', url)
    if match:
        return match.group(1), match.group(2), match.group(3)

    match = re.search('^https?://s3.amazonaws.com/([^\/]+)/(.+)', url)
    if match:
        return match.group(1), None, match.group(2)

    match =  re.search('^https?://s3-([^.]+).amazonaws.com/([^\/]+)/(.+)', url)
    if match:
        return match.group(2), match.group(1), match.group(3)

    return None, None, None
