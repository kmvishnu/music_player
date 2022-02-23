import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import FavoriteTwoToneIcon from '@mui/icons-material/FavoriteTwoTone';
import { Button } from '@mui/material';
import axios from 'axios';
import { useDispatch, useSelector } from 'react-redux';
import { ADDFAV, USERDETAILS } from '../store/constants/storeConstants';
import { useState,useEffect } from 'react';
import AddIcon from '@mui/icons-material/Add';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';

import "./Playlist.css";


export default function BasicTable(props) {
  
const songs =props.songs
const SetCurrentSong=props.SetCurrentSong
const keyword =props.keyword
const UserDetails =useSelector(state=>state.UserDetails)
const dispatch = useDispatch()
const User =useSelector(state=>state.currentUser)
const showFav =useSelector(state=>state.showFav)
const allFav = useSelector(state=>state.UserDetails.favourite)
const [visible,setVisible] = useState(false)
console.log("showFav:",showFav,"Allfav:",allFav)
const [modal, setModal] = useState(false);

const toggleModal = () => {
  setModal(!modal);
};



useEffect(()=>{
  axios.get("http://127.0.0.1:5001/getUser/"+User.email).then(
      (response)=>{
        dispatch({type:USERDETAILS,payload:response.data})
      }).catch(
          error=>console.log(error))}
          ,[])


console.log("UserDetails:",UserDetails)
console.log("favourites before button click: ",UserDetails['favourite'])
const fav = (x) =>{
 

  if (UserDetails['favourite'].includes(x)){
    let index = UserDetails['favourite'].indexOf(x)
    UserDetails['favourite'].splice(index,1)
    dispatch({type:ADDFAV,payload:UserDetails['favourite']})
    let f2 = {"email":UserDetails.email,"favourite":UserDetails['favourite']}
    axios.put("http://127.0.0.1:5001/addFav",f2).then((response)=>{
    }).catch(error=>console.log(error))
    console.log("favourites after deleting:",UserDetails['favourite'])
  }else{
    UserDetails['favourite'].push(x)
    dispatch({type:ADDFAV,payload:UserDetails['favourite']})
    const f2 = {"email":UserDetails.email,"favourite":UserDetails['favourite']}
    axios.put("http://127.0.0.1:5001/addFav",f2).then((response)=>{
    }).catch(error=>console.log(error))  
    console.log("favourites after adding:",UserDetails['favourite'])
  }}

 
  if(!showFav){
    return (
      <>
      {modal && (
        <div className="modal">
          <div onClick={toggleModal} className="overlay"></div>
          <div className="modal-content">
            
                                  <Box sx={{ minWidth: 120 }}>
                              <FormControl fullWidth>
                                <InputLabel id="demo-simple-select-label">Playlist</InputLabel>
                                <Select
                                  labelId="demo-simple-select-label"
                                  id="demo-simple-select"
                                  
                                  label="Playlist"
                                 
                                >
                                  {UserDetails.playlist.map()}
                                  {/* <MenuItem value={10}>Ten</MenuItem>
                                  <MenuItem value={20}>Twenty</MenuItem>
                                  <MenuItem value={30}>Thirty</MenuItem> */}
                                </Select><br/>
                                <TextField id="standard-basic" label="Enter New Playlist" variant="standard" />
                                <Button>Add Playlist</Button>
                              </FormControl>
                            </Box>
            
          </div>
        </div>
      )}
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
        
          <TableBody>
            {songs.filter((val)=>{
              if(keyword==='')
              {
                return val
              }
              else if(
                val.name.toLowerCase().includes(keyword.toLowerCase()) ||
                val.author.toLowerCase().includes(keyword.toLowerCase())
              )
              {
                return val
              }
              
            }).map((row,index) => (
             
              <TableRow
                key={index+1}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
               
              >
                
                <TableCell align="right" >
                  <Button onClick={()=>SetCurrentSong(row.id)}><img src={row.links.images[0].url} width={60} height={60} alt="artist"/></Button>
                </TableCell>
                <TableCell align="left"><b>{row.name}</b><br/>{row.author}</TableCell>
                <TableCell align="left">
                  <Button type="button"  onClick={()=>fav(row.id)}><FavoriteTwoToneIcon/></Button>
                  <Button variant="text" onClick={()=>toggleModal()}><AddIcon/></Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      </>
    );
  }
  else{
    return (
      <>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
        
          <TableBody>
            {songs.filter((val)=>{
              if(keyword==='')
              {
                if(allFav.includes(val.id)){
                  return val
                }
              }
              else if(
                val.name.toLowerCase().includes(keyword.toLowerCase()) ||
                val.author.toLowerCase().includes(keyword.toLowerCase())
              )
              {
                if(allFav.includes(val.id)){
                  return val
                }
              }
              
            }).map((row,index) => (
             
              <TableRow
                key={index+1}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
               
              >
                
                <TableCell align="right" >
                  <Button onClick={()=>SetCurrentSong(row.id)}><img src={row.links.images[0].url} width={60} height={60} alt="artist"/></Button>
                
                </TableCell>
                <TableCell align="left"><b>{row.name}</b><br/>{row.author}</TableCell>
                <TableCell align="left">
                  <Button type="button"  onClick={()=>fav(row.id)}><FavoriteTwoToneIcon/></Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      </>
    );
    }
  }

