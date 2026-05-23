def lambda_handler(event, context):

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Lambda Frontend</title>
    </head>

    <body style="
        margin:0;
        padding:0;
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
        background:linear-gradient(to right, #141e30, #243b55);
        font-family:Arial, sans-serif;
    ">

        <div style="
            background:white;
            padding:40px;
            border-radius:12px;
            box-shadow:0 0 15px rgba(0,0,0,0.3);
            text-align:center;
        ">

            <h1 style="
                color:#243b55;
                margin-bottom:15px;
            ">
                Frontend Deployed Using AWS Lambda
            </h1>

            <p style="
                color:gray;
                font-size:18px;
            ">
                Serverless Deployment Successful
            </p>

        </div>

    </body>
    </html>
    """

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html_content
    }