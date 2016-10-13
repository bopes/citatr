$(document).ready(function(){

  // 1. DOM Elements

    $inputForm = $('#input_form');
    $inputText = $('#input_text');
    $inputPages = $('#input_pages');

    $loadingGif = $('#loading_gif');

    $conversionError = $('#conversion_error');
    $convertedCitation = $('#converted_citation');

  // 2. Method definitions

    // A. Citation Conversion/AJAX

      var receiveCitationInput = function(event){
        event.preventDefault();
        clearConversionContainer();
        showLoadingGif();
        inputData = $inputForm.serialize();
        setTimeout(convertInput,750,inputData);
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

    // B. DOM Manipulation

      // i. Conversion Container
        var clearConversionContainer = function(){
          hideConversionError();
          hideConvertedCitation();
          hideLoadingGif();
        };

      // ii. Converted Citation
        var displayConvertedCitation = function(citationText){
          $convertedCitation.html(citationText);
          $convertedCitation.show();
        };

        var hideConvertedCitation = function(){
          $convertedCitation.hide();
        };

      // iii. Conversion Error
        var displayConversionError = function(){
          clearConversionContainer();
          $conversionError.show();
        };

        var hideConversionError = function(){
          $conversionError.hide();
        };

      // iv. Loading Gif
        var showLoadingGif = function(){
          $loadingGif.show();
        };

        var hideLoadingGif = function(){
          $loadingGif.hide();
        };

    // C. jQuery Listeners
      var setupChangeListeners = function(){
        $inputText.on('change',receiveCitationInput);
        $inputPages.on('change',receiveCitationInput);
      };

  // 3. Live code

    $inputForm.on('submit',receiveCitationInput);

});