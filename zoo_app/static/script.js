//formのinput[type="file"]が変更時の処理
$(document).on('change', ':file', function() {
    // input[type="file"]のファイル名をinput[type="text"]に表示する処理
    var input = $(this);
    numFiles = input.get(0).files ? input.get(0).files.length : 1;
    label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.parent().parent().prev(':text').val(label);
    
    $('form').submit();
    //Ajaxはここから
    // $.ajax({
    //     url: $("#form").attr("action"),
    //     type: 'POST',
    //     data: new FormData($("#form").get(0)),
    //     processData: false,
    //     contentType: false,
    //     beforeSend: function(xhr, settings) {
    //        //リクエスト送信前の処理
    //        // CSRFTokenを設定したり、前の結果を削除したり、ローディングを表示したり
    //        xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
    //        $('#result-table').empty();
    //        $("#loading-div").show();
    //     },
    // }).done(function(data, textStatus, jqXHR){
    //     // 成功したら、結果を追加する
    //     $tbody.append($(data));
    // }).fail(function(jqXHR, textStatus, errorThrown){
    //     // 失敗したら、コンソールにログを吐く
    //     console.log(jqXHR + "\n" + textStatus + "\n" + errorThrown);
    // }).always(function(data, textStatus, jqXHR){
    //     // 成功しても、失敗しても、レスポンスが返ってきたら、ローディングを非表示にする
    //     $("#loading-div").hide();
    // });
  });

  $(document).on('change', ':file', function() {
    var input = $(this),
    numFiles = input.get(0).files ? input.get(0).files.length : 1,
    label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.parent().parent().next(':text').val(label);

    var files = !!this.files ? this.files : [];
    if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support
    if (/^image/.test( files[0].type)){ // only image file
        var reader = new FileReader(); // instance of the FileReader
        reader.readAsDataURL(files[0]); // read the local file
        reader.onloadend = function(){ // set image data as background of div
            input.parent().parent().parent().prev('.imagePreview').css("background-image", "url("+this.result+")");
        }
    }
});