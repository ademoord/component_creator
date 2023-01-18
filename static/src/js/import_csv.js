// odoo.define('component_creator', function (require) {
//     "use strict";
//     var core = require('web.core');
//     var _t = core._t;
//     var $ = core.$;
//     jQuery(document).ready(function () {
//         jQuery('.o_button_upload_alkeba').on('click', function () {
//             jQuery('input[type="file"]').click();
//         });
//     });
// });

odoo.define('component_creator', ['jquery'], function (require) {
    "use strict";
    var $ = require('jquery');
    $(document).on('click', '.o_button_upload_alkeba', function(event){
        jQuery('input[type="file"]').click();
    });
});
