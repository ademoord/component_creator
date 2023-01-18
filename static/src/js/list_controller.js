// odoo.define('component_creator.list_controller', function (require) {
//     "use strict";

//     var ListController = require('web.ListController');
//     var core = require('web.core');
//     var _t = core._t;

//     ListController.include({
//         renderButtons: function () {
//             var self = this;
//             this._super.apply(this, arguments);
//             if (this.modelName === 'service.master') {
//                 this.$buttons.find('.o_list_button_add').after(
//                     $('<button>', {
//                         class: 'btn btn-primary btn-sm o_list_button_upload_alkeba',
//                         accesskey: 'f',
//                         text: _t("Import CSV JS"),
//                         console.log(self.$('input[type=file]'));
//                     }).click(function () {
//                         self.$('input[type=file]').click();
//                     })
//                 );
//             }
//         },
//     });
//     core.action_registry.add('component_creator.list_controller', ListController);
//     // return the object
//     return ListController;
// });


// odoo.define('component_creator.import_csv', function (require) {

//     "use strict";       
//     var core = require('web.core');
//     var ListView = require('web.ListView'); 
//     var ListController = require("web.ListController");
    
//     var includeDict = {
//         renderButtons: function () {
//             this._super.apply(this, arguments);
//             if (this.modelName === "item.master") {
//                 var your_btn = this.$buttons.find('button.o_list_button_add')
//                 your_btn.on('click', this.proxy('o_list_button_add'))
//             }
//         },
//         o_list_button_add: function(){
//         }
//     };
//     ListController.include(includeDict);
// });



// odoo.define('component_creator.service.master', function (require) {
//     "use strict";

//         var core = require('web.core');
//         var ListController = require('web.ListController');
//         var ListView = require('web.ListView');
//         var UploadFile = require('account.upload.bill.mixin');
//         var viewRegistry = require('web.view_registry');
    
//         var ServiceListController = ListController.extend(UploadBillMixin, {
//             buttons_template: 'ServiceListView.buttons',
//             events: _.extend({}, ListController.prototype.events, {
//                 'click .o_list_button_upload_alkeba': '_onUpload',
//                 'change .o_vendor_bill_upload .o_form_binary_form': '_onAddAttachment',
//             }),
//         });
    
//         var ServiceListView = ListView.extend({
//             config: _.extend({}, ListView.prototype.config, {
//                 Controller: ServiceListController,
//             }),
//         });
    
//         viewRegistry.add('service_master', ServiceListView);
// });
