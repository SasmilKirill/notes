import {useLocation} from "react-router-dom";

import React from "react


const NotFound404= () => {
    let {pathname} = useLocation()
    return(
       <div>
           <hi>Page not found {pathname} </h1>
       </div>
    )
}

export default NotFound404