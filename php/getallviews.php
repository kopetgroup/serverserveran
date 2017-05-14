<?php
$db   = 'zabei_net';
$r    = file_get_contents('http://5.189.157.134:5984/'.$db.'/_all_docs?startkey=%22_design/%22&endkey=%22_design0%22');
$r    = json_decode($r);

foreach($r->rows as $c){
  echo 'http://5.189.157.134:5984/'.$db.'/'.$c->key.'/'.str_replace('_design','_view',$c->key).'?limit=1&update_seq=true<br/>';
}


//afternine_net//get_subcategory/_view/get_subcategory
