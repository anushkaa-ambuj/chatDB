import { Routes } from '@angular/router';
import { ChatdbComponent } from '../pages/chatdb/chatdb.component';
import { HomeComponent } from '../pages/home/home.component';
import { AboutComponent } from '../pages/about/about.component';
import { ContactComponent } from '../pages/contact/contact.component';

export const routes: Routes = [
    {path:'', redirectTo: 'chatDB', pathMatch: 'full'},
    {path:'chatDB', component: ChatdbComponent},
    {path:'home', component: HomeComponent},
    {path:'about', component: AboutComponent},
    {path:'contact', component: ContactComponent},
];
