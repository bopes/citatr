$(document).ready(function(){

  $inputForm = $('#input_form');
  $inputText = $('#input_text');
  $inputPages = $('#input_pages');

  $loadingGif = $('#loading_gif');

  $conversionError = $('#conversion_error');
  $convertedCitation = $('#converted_citation');


  var receiveCitationInput = function(event){
    event.preventDefault();
    showLoadingGif();
    inputData = $inputForm.serialize();
    setTimeout(sendInputToConverter,750,inputData);
  };

  var sendInputToConverter = function(input){
    convertInput(input);
  };

  var convertInput = function(input){
    ajaxObj = {url: '/convert', data: input};
    $.ajax(ajaxObj)
      .done(receiveConvertedCitation)
      .fail(displayConversionError);
  };

  var receiveConvertedCitation = function(data){
    finalCitation = data['finalCitation'];
    displayConvertedCitation(finalCitation);
    hideLoadingGif();
    setupChangeListeners();
  };

  var displayConvertedCitation = function(citationText){
    $conversionError.hide();
    $convertedCitation.show();
    $convertedCitation.text(citationText);
  };

  var setupChangeListeners = function(){
    $inputText.on('change',receiveCitationInput);
    $inputPages.on('change',receiveCitationInput);
  };

  var displayConversionError = function(){
    $convertedCitation.hide();
    $conversionError.show();
    hideLoadingGif();
  };

  var showLoadingGif = function(){
    $loadingGif.show();
  };

  var hideLoadingGif = function(){
    $loadingGif.hide();
  };

  $inputForm.on('submit',receiveCitationInput);

});