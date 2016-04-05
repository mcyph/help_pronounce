
var enunciating = {
    init: function() {
        $('#search-input').keypress($.proxy(this.onSearchChange, this));
        $('#search-input').keydown($.proxy(this.onSearchChange, this));
    },

    onSearchChange: function() {
        setTimeout($.proxy(this._onSearchChange, this), 0);
    },

    _onSearchChange: function() {
        var value = $('#search-input')[0].value;

        $.ajax({
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
