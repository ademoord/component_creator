// odoo.define('component_creator.import_csv', function (require) {
//     "use strict";

//     var ListController = require('web.ListController');
//     var core = require('web.core');
//     var _t = core._t;

//     ListController.include({
//         renderButtons: function () {
//             var self = this;
//             this._super.apply(this, arguments);
//             if (this.modelName === 'item.master') {
//                 this.$buttons.find('.o_list_button_upload').after(
//                     $('<button>', {
//                         class: 'btn btn-primary btn-sm o_list_button_upload',
//                         accesskey: 'f',
//                         text: _t("Import CSV"),
//                     }).click(function () {
//                         self.$('input[type=file]').click();
//                     })
//                 );
//             }
//         },
//     });
//     core.action_registry.add('component_creator.import_csv', ListController);
//     // return the object.
//     return ListController;
// });


odoo.define('component_creator.import_csv', function (require) {

    "use strict";       
    var core = require('web.core');
    var ListView = require('web.ListView'); 
    var ListController = require("web.ListController");
    
    var includeDict = {
        renderButtons: function () {
            this._super.apply(this, arguments);
            if (this.modelName === "item.master") {
                var your_btn = this.$buttons.find('button.o_list_button_add')
                your_btn.on('click', this.proxy('o_list_button_add'))
            }
        },
        o_list_button_add: function(){
        }
    };
    ListController.include(includeDict);
});