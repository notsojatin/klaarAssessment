> outputCurl.txt
for i in $(cat curlURLs.txt); 
    do
        content=$(curl -s "{$i}")
        echo "URL: $i" >> outputCurl.txt
        echo "$content" >> outputCurl.txt
        echo "--------------------------------" >> outputCurl.txt
done