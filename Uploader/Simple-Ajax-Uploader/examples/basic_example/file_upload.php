<?php
require('extras/Uploader.php');

// Directory where we're storing uploaded images
// Remember to set correct permissions or it won't work
$upload_dir = '/var/www/html/GITHUB/Uploader/Simple-Ajax-Uploader/upload_files';

$uploader = new FileUpload('uploadfile');

// Handle the upload
$result = $uploader->handleUpload($upload_dir);

if (!$result) {
  exit(json_encode(array('success' => false, 'msg' => $uploader->getErrorMsg())));
}

echo json_encode(array('success' => true));
