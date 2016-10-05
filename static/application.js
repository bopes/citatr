$(document).ready(function(){

  $inputDiv = $('#input')
  $inputForm = $('#input_form');
  $inputText = $('#input_text');
  $inputPages = $('#input_pages')

  $outputDiv = $('#output')
  $convertedCitation = $('#converted_citation');

  var receiveCitationInput = function(event){
    event.preventDefault();
    $form = $(this);
    $.ajax({
      url: '/convert',
      data: $inputForm.serialize()
    })
      .done(
        receiveConvertedCitation
      );
  };

  var receiveConvertedCitation = function(data){
    displayConvertedCitation(data['finalCitation']);
  };

  var displayConvertedCitation = function(citationText){
    $outputDiv.show();
    $convertedCitation.text(citationText);
  };

  $inputForm.on('submit',receiveCitationInput);
  $inputText.on('change',receiveCitationInput)
  $inputPages.on('change',receiveCitationInput)

})