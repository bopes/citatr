$(document).ready(function(){

  $inputForm = $('#input_form');
  $inputText = $('#input_text');
  $inputPages = $('#input_pages');

  $loadingGif = $('#loading_gif');

  $conversionError = $('#conversion_error');
  $convertedCitation = $('#converted_citation');


  var receiveCitationInput = function(event){
    event.preventDefault();
    clearConversionContainer();
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
    clearConversionContainer();
    displayConvertedCitation(finalCitation);
    setupChangeListeners();
  };

  var displayConvertedCitation = function(citationText){
    $convertedCitation.text(citationText);
    $convertedCitation.show();
  };

  var hideConvertedCitation = function(){
    $convertedCitation.hide();
  };

  var displayConversionError = function(){
    clearConversionContainer();
    $conversionError.show();
  };

  var hideConversionError = function(){
    $conversionError.hide();
  };

  var showLoadingGif = function(){
    $loadingGif.show();
  };

  var hideLoadingGif = function(){
    $loadingGif.hide();
  };

  var clearConversionContainer = function(){
    hideConversionError();
    hideConvertedCitation();
    hideLoadingGif();
  };

  var setupChangeListeners = function(){
    $inputText.on('change',receiveCitationInput);
    $inputPages.on('change',receiveCitationInput);
  };

  $inputForm.on('submit',receiveCitationInput);

});