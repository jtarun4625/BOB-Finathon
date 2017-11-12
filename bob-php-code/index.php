<?php 

$method = $_SERVER['REQUEST_METHOD'];

// Process only when method is POST
if($method == 'POST'){
  $requestBody = file_get_contents('php://input');
  $json = json_decode($requestBody);

  $text = $json->result->parameters->City;


$ch = curl_init();
$url = '';

$headers = array();
$headers[] = 'content-type: application/json';
$headers[] = 'accept-encoding: gzip,deflate';
$headers[] = 'apikey: 844A1851T96625UA';

curl_setopt($ch, CURLOPT_URL,"http://104.211.176.248:8080/bob/bobuat/api/CitywiseSearch");

curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$data_string = json_encode(array("city"=>$text));
curl_setopt($ch, CURLOPT_POSTFIELDS,$data_string);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$server_output = curl_exec ($ch);

curl_close ($ch);
if ($server_output == "OK") { 
  $speech = "Searching For Address";

  $response = new \stdClass();
  $response->speech = $speech;
  $response->displayText = $speech;
  $response->source = "webhook";
  echo json_encode($response);
} else {
  $speech = "";
    $main_array = json_decode($server_output, true);
    $list = array();
    $i=0;
    foreach ($main_array as $key => $value){
      if($i==4)break;
      foreach ($value as $key2 => $value2){
        if($key2=="Name"){
          $name = $value2;
        }elseif ($key2=="address") {
          $address = $value2;
        }
      }
      $speech = $name ."Branch ------------ > "."".$address."";
      // $d[] = array('type' => "0" ,'speech' => "$speech");
      $i++;
    }
  $response = new \stdClass();
  $response->speech = $speech;
  $response->messages = $d;
  // $response->displayText = $d;
  $response->source = "webhook";
  echo json_encode($response);
}

}
else
{
  echo "Method not allowed";
}

?>