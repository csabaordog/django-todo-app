import {useEffect, useState} from 'react';

import './App.css';

type Task = {
  id?: number;
  title: string;
  description: string;
  created_at?: string;
  due_date: string;
  status: string;
};



function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTask, setNewTask] = useState<Task>({ title: '', description: 'sample desc', due_date: new Date().toISOString(), status: 'PENDING' });
  
  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try{
      const response = await fetch('http://localhost:8000/task/task-list/');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data: Task[] = await response.json();

      setTasks(data);
    }
    catch(error){
      console.error(error);
    }
  }

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setNewTask({ ...newTask, [name]: value });
  };


  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/task/task-create/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newTask),
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const createdTask: Task = await response.json();
      setTasks([...tasks, createdTask]);
      setNewTask({ title: '', description: '', due_date: new Date().toISOString(), status: 'PENDING' });
    } catch (error) {
      console.error('Error creating task:', error);
    }
  };

  const handleCheckboxChange = async (taskId: number) => {
    const updatedTasks = tasks.map(task => {
      if (task.id === taskId) {
        
        task.status = task.status === 'PENDING' ? 'COMPLETED' : 'PENDING';
      }
      return task;
    });
    setTasks(updatedTasks);

    try {
      const taskToUpdate = updatedTasks.find(task => task.id === taskId);
      await fetch(`http://localhost:8000/task/task-update/${taskId}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskToUpdate),
      });
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  

  return (
    <div className="App">
      <div className="container">

        <h1 className='page-title'>To Do App</h1>
        <div className='form-container'>
          <form onSubmit={handleSubmit}>
            
            <input id="title" name="title" type="text" placeholder="Enter a task" value={newTask.title}  onChange={handleInputChange}/>              
          
            <input id="submit" name="submit" type="submit" value="+"/>
        
          </form>
        </div>
        <hr className="custom-hr"/>
        
        <div className="tasks-container"> 
        {tasks.map((task, index) => (

            <div key={index} className="task-item">
              <div className="task-status">
                <input
                  type="checkbox"
                  checked={task.status === 'COMPLETED'}
                  onChange={() => task.id && handleCheckboxChange(task.id)}
                  style={{ transform: 'scale(1.5)' }}
                />
              </div>
              
              <div className="task-details">
                {task.title}
              </div>

              <div></div>
              
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}

export default App;
