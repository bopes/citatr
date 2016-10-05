$(document).ready(function(){

  $inputDiv = $('#input')
  $inputForm = $('#input_form');
  $inputText = $('#input_text');
  $inputPages = $('#input_pages')

  $loadingGif = $('#loading_gif')

  $outputDiv = $('#output')
  $convertedCitation = $('#converted_citation');

  var receiveCitationInput = function(event){
    event.preventDefault();
    showLoadingGif();
    $.ajax({
      url: '/convert',
      data: $inputForm.serialize()
    })
      .done(
        receiveConvertedCitation
      );
  };

  var receiveConvertedCitation = function(data){
    hideLoadingGif();
    displayConvertedCitation(data['finalCitation']);
    setupChangeListeners();
  };

  var setupChangeListeners = function(){
    $inputText.on('change',receiveCitationInput)
    $inputPages.on('change',receiveCitationInput)
  };

  var displayConvertedCitation = function(citationText){
    $outputDiv.show();
    $convertedCitation.text(citationText);
  };

  var showLoadingGif = function(){
    $loadingGif.show();
  };

  var hideLoadingGif = function(){
    $loadingGif.hide();
  };

  $inputForm.on('submit',receiveCitationInput);

})