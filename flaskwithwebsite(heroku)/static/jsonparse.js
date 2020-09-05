// Get the GitHub username input form


function requestUserRepos(){
    
    // Create new XMLHttpRequest object
    
    // When request is received
    // Process it here
    xhr.onload = function () {
    
        // Parse API data into JSON
        const data = {final};
        // Loop over each object in data array
      
            // Get the ul with id of of userRepos
            let ul = document.getElementById('userRepos');
    
            // Create variable that will create li's to be added to ul
            let li = document.createElement('p');
            
            // Add Bootstrap list item class to each li
            li.classList.add('list-group-item')
        
            // Create the html markup for each li
            li.innerHTML = (`
                <p>⭐ <strong>Total stars:   </strong>${data['Academic Year']}</p>
                <p>🍴 <strong>Total forks:  </strong> ${data['Subject Code']}</p>
                <p><i class="fa fa-bug" style="font-size:24px;color:red"></i><strong>   Total open issues:     </strong> ${data['Total Class']}</p>
            `);
            
            // Append each li to the ul
            ul.appendChild(li);
        

    }
    
    // Send the request to the server
    xhr.send();
    
}
requestUserRepos();