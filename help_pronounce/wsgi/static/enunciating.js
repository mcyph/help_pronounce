var xhr = null;


var enunciating = {
    init: function() {
        var fn = $.proxy(this.onSearchChange, this);
        $('#search-input').val('');
        $('#search-input').keypress(fn);
        $('#search-input').keydown(fn);
        $('#search-input').on('change', fn);
        $('#search-input').on('reset', fn);
        $('#search-input').click(fn);
        $('#search-input').focus();
    },

    onSearchChange: function() {
        setTimeout($.proxy(this._onSearchChange, this), 0);
    },

    _onSearchChange: function() {
        var value = $('#search-input')[0].value;
        if (this.curVal == value) {
            return;
        }
        this.curVal = value;

        $.trim(value) ? $('#logo').hide() : $('#logo').show();
        $('#logo').addClass('notransition');
        document.documentElement.scrollTop = 0;
        document.title = !$.trim(value) ?
            'HelpPronounce.com - find pronunciations and phonemes quickly!' :
            'HelpPronounce.com - '+$.trim(value);

        if (xhr) {
            xhr.abort();
        }

        xhr = $.ajax({
            url: "/dynamic?q="+encodeURIComponent(value),
            success: function(result) {
                $("#dynamic").html(result);
            }
        });
    },

    play: function(id1, id2) {
        var audio = $('#audio'+id1+'_'+id2)[0];
        audio.play();
    }
}

$(document).ready($.proxy(enunciating.init, enunciating));
