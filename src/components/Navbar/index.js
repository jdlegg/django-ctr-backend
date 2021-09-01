import React from 'react';
import { 
  Nav,
  NavLink,
  Bars,
  NavMenu,
  NavBtn,
  NavBtnLink,
} from './NavbarElements';
  
const Navbar = (props) => {
    return (
        <>
        <Nav>
            <Bars />
            <NavMenu>
                {(!props.isAuth) && (<NavLink to='/signup' activeStyle> Signup </NavLink>)}
                {(props.isAuth) && (<NavLink to='/protected' activeStyle>Protected View inside Auth </NavLink>)}
                {(props.isAuth) && (<NavLink to='/highscore' activeStyle>High Score </NavLink>)}
                {(props.isAuth) && (<NavLink to='/ind_score' activeStyle>Individual Score </NavLink>)}
                {(props.isAuth) && (<NavLink to='/challenge1' activeStyle>Challenge 1 </NavLink>)}
                {(props.isAuth) && (<NavLink to='/register' activeStyle>Register Challenge </NavLink>)}
                {/* Second Nav */}
                {/* <NavBtnLink to='/sign-in'>Sign In</NavBtnLink> */}
            </NavMenu>
            <NavBtn>
                {(props.isAuth) ? (<NavBtnLink to='/logout'>Logout</NavBtnLink>) : (<NavBtnLink to='/login'>Login</NavBtnLink>)}
            </NavBtn>
        </Nav>
        </>
  );
};
  
export default Navbar;