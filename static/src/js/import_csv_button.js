function submit_form(){
    let input = document.querySelector('input[type="file"]');
    let file = input.files[0];
    if(file){
        let reader = new FileReader();
        reader.onload = function(){
            let fileContent = reader.result;
            // parse the csv file content
            let data = Papa.parse(fileContent,{
                header: true,
                dynamicTyping: true
            });
            // send the parsed data to the server
            rpc.query({
                model: 'component_creator.item_master',
                method: 'action_import_csv',
                args: [data],
            }).then(function (result) {
                console.log(result);
            });
        }
        reader.readAsText(file);
    }
}
