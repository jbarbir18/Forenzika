    function readLocalFile(callback) {
      const fileInput = document.createElement('input');
      fileInput.type = 'file';

      fileInput.onchange = function(event) {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function() {
          const fileContent = reader.result;

          try {
            const data = JSON.parse(fileContent);
            callback(null, data);
          } catch (error) {
            callback(error);
          }
        };

        reader.readAsText(file);
      };

      fileInput.click();
    }

    const button = document.getElementById('readFileButton');
    const output = document.getElementById('output');

    button.addEventListener('click', function() {
      readLocalFile(function(error, data) {
        if (error) {
          console.error('Error:', error);
        } else {
          output.textContent = JSON.stringify(data);
          // You can also display specific properties from the data object
          // by accessing them and updating the output accordingly
        }
      });
    });

    