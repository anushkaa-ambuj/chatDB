import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChatdbComponent } from './chatdb.component';

describe('ChatdbComponent', () => {
  let component: ChatdbComponent;
  let fixture: ComponentFixture<ChatdbComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ChatdbComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ChatdbComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
