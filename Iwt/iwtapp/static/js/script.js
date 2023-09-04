fetch("static/js/balu.json")
.then(function(response){
   return response.json();
})
.then(function(products){
   let placeholder = document.querySelector("#data-output");
   let out = "";
   for(let product of products){
      out += `
         <tr>
            <td> <img src="https://icon-library.com/images/user-profile-icon/user-profile-icon-24.jpg"> </td>
            <td>${product.name}</td>
            <td>${product.email}</td>
            <td>${product.mobile}</td>
            <td>${product.userCode}</td>
         </tr>
      `;
   }
   placeholder.innerHTML = out;
})