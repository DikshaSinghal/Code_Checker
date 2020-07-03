const express = require('express')
const app = express()
const morgan = require('morgan')

app.use(morgan('short'))
//localhost:3004
app.get("/",(req,res)=>{
  res.send("hello there!")
})
app.get("/mylist",(req,res)=>{
  var list1 = {todo: "drink"}
  res.json(list1)
  // res.send("Add here")
})
app.listen(3004, () =>{
  console.log("server listening on 3004...")
})
