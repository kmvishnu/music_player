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
import SimpleDialog from './Playlist';
import Typography from '@mui/material/Typography';
import AddIcon from '@mui/icons-material/Add';

export default function BasicTable(props) {
  
 // ==========================================================
  const emails = ['username@gmail.com', 'user02@gmail.com'];
  const [open, setOpen] = React.useState(false);
  const [selectedValue, setSelectedValue] = React.useState(emails[1]);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = (value) => {
    setOpen(false);
    setSelectedValue(value);
  };
  // ==========================================================

const songs =props.songs
const SetCurrentSong=props.SetCurrentSong
const keyword =props.keyword
const UserDetails =useSelector(state=>state.UserDetails)
const dispatch = useDispatch()
const User =useSelector(state=>state.currentUser)
const showFav =useSelector(state=>state.showFav)
const allFav = useSelector(state=>state.UserDetails.favourite)
console.log("showFav:",showFav,"Allfav:",allFav)


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
 

 

  if(showFav){
  return (
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
              <TableCell>   
                  <div>
                    <Button variant="outlined" onClick={handleClickOpen}>
                    <AddIcon/>
                    </Button>
                    <SimpleDialog
                      selectedValue={selectedValue}
                      open={open}
                      onClose={handleClose}
                    />
                  </div>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
  }
  else{
    return (
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
                </TableCell>
                <TableCell>   
                  <div>
                    <Button variant="outlined" onClick={handleClickOpen}>
                    <AddIcon/>
                    </Button>
                    <SimpleDialog
                      selectedValue={selectedValue}
                      open={open}
                      onClose={handleClose}
                    />
                  </div>
              </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    );
  }
}
